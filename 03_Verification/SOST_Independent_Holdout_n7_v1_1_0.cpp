#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

static inline int pc(uint32_t x){return __builtin_popcount(x);}

int main(){
    constexpr int n=7,m=21; constexpr uint32_t N=1u<<m;
    int idx[n][n]; for(int i=0;i<n;i++)for(int j=0;j<n;j++)idx[i][j]=-1;
    std::vector<uint8_t> endpoints; int e=0;
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){idx[i][j]=idx[j][i]=e++;endpoints.push_back(static_cast<uint8_t>((1u<<i)^(1u<<j)));}
    std::vector<uint32_t> tri;
    for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)tri.push_back((1u<<idx[a][b])|(1u<<idx[a][c])|(1u<<idx[b][c]));
    auto key=[&](uint32_t x){uint8_t p=0;for(int k=0;k<m;k++)if((x>>k)&1u)p^=endpoints[k];return static_cast<int>(p)*3+pc(x)%3;};
    std::vector<uint8_t> seen(N,0); std::array<int,384> key_comp; key_comp.fill(-1); std::vector<uint32_t> q; q.reserve(65536);
    int comps=0,keys=0,mismatch=0; uint64_t legal=0;
    for(uint32_t s=0;s<N;s++){
        if(seen[s])continue;int cid=comps++,ckey=key(s);
        if(key_comp[ckey]==-1){key_comp[ckey]=cid;keys++;}else if(key_comp[ckey]!=cid)mismatch++;
        q.clear();q.push_back(s);seen[s]=1;size_t h=0;
        while(h<q.size()){
            uint32_t x=q[h++];if(key(x)!=ckey)mismatch++;
            for(uint32_t mask:tri){uint32_t z=x&mask;if(z==0u||z==mask){legal++;uint32_t y=x^mask;if(!seen[y]){seen[y]=1;q.push_back(y);}}}
        }
    }
    std::cout<<"{\"algorithm\":\"independent_flood_fill\",\"n\":7,\"states\":"<<N<<",\"components\":"<<comps<<",\"invariant_keys\":"<<keys<<",\"mismatches\":"<<mismatch<<",\"legal_state_triangle_checks\":"<<legal<<"}"<<std::endl;
    return (comps==192&&keys==192&&mismatch==0&&legal==18350080ULL)?0:1;
}

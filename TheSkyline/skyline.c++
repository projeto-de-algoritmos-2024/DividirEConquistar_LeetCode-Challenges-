class Solution {
public:
typedef pair<int,int> PI;
    vector<vector<int>> getSkyline(vector<vector<int>>& b) {
        int n=b.size();
        map<int,vector<PI>> mp;
        vector<vector<int>> ans;
        int ind=0;
        for(auto& ele: b){
            mp[ele[0]].push_back({0,ind});
            mp[ele[1]].push_back({1,ind});
            ind++;
        }
        set<PI> st;
        for(auto& [x,vec]: mp){
            for(auto& [state,ind]: vec){
                if(state){
                    st.erase({b[ind][2],ind});
                }
                else{
                    st.insert({b[ind][2],ind});
                }
            }
            int u=x;
            int v;
            if(st.size()) v=(--st.end())->first;
            else v=0;
            if(!ans.size() || ans.back()[1]!=v) ans.push_back({u,v});
        }
        
        return ans;
    }
};
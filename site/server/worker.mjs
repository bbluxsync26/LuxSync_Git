import {api} from './api.mjs';
export default {
  async fetch(request,env) {
    const answer=await api(request,env);
    if(answer)return answer;
    return env.ASSETS.fetch(request);
  }
};

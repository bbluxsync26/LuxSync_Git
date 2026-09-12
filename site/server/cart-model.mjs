export function applyCartAction(current, action, knownSkus) {
  const items=structuredClone(current);
  const fail=message=>{throw new Error(message);};
  if (!action || typeof action!=='object') fail('Choose a cart action.');
  if (action.action==='import') {
    if (!Array.isArray(action.items)||action.items.length>100) fail('Invalid previous cart.');
    for(const old of action.items) {
      if(!old||typeof old.id!=='string'||old.id.length>100||typeof old.name!=='string')continue;
      if(items.some(i=>i.id===old.id))continue;
      if(knownSkus.has(old.id)){items.push({id:old.id,sku:old.id,quantity:1});continue;}
      const strings=value=>Array.isArray(value)?value.filter(v=>typeof v==='string').slice(0,30).map(v=>v.slice(0,200)):[];
      items.push({id:old.id,kind:'blueprint',name:old.name.slice(0,160),foundation:String(old.foundation||'').slice(0,500),experiences:strings(old.experiences),families:strings(old.families),quantity:1});
    }
  } else {
    const id=action.sku||action.id;
    const index=items.findIndex(i=>i.id===id);
    if(action.action==='remove'){if(index>=0)items.splice(index,1);}
    else if(action.action==='add' || action.action==='quantity'){
      const quantity=action.quantity;
      if(!Number.isInteger(quantity)||quantity<1||quantity>99)fail('Choose a quantity from 1 to 99.');
      if(action.action==='add'){
        if(!knownSkus.has(id))fail('This item is not in the catalog.');
        if(index>=0){if(items[index].quantity+quantity>99)fail('A cart line can contain up to 99 items.');items[index].quantity+=quantity;}
        else items.push({id,sku:id,quantity});
      }else{if(index<0)fail('This cart line was not found.');items[index].quantity=quantity;}
    }else fail('Unknown cart action.');
  }
  if(items.length>100)fail('A cart can contain up to 100 different items.');
  return items;
}

export function validWishlist(data, knownSkus) {
  return !!data && Object.keys(data).every(key=>key==='items') && Array.isArray(data.items) && data.items.length<=100
    && new Set(data.items.map(i=>i?.sku)).size===data.items.length
    && data.items.every(i=>i && knownSkus.has(i.sku) && Number.isInteger(i.quantity) && i.quantity>=1 && i.quantity<=99);
}

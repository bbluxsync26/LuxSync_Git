export function iconFor(title = '') {
  const exact = {
    'Curated technology':'automation-home-gear',
    'Make an informed plan':'calendar',
    'Real people. Clear answers.':'support-headset',
    'Intelligent Opening':'calendar',
    'Accessible Living':'automation-home-gear',
    'Water Watch':'security-shield-check',
    'Welcome Home':'automation-home-gear',
    'Goodnight':'lighting-bulb'
  };
  if (exact[title]) return exact[title];
  const rules = [
    ['shades-window', /shade|window|blind/i],
    ['energy-bolt', /energy|power/i],
    ['camera', /camera/i],
    ['security-shield-check', /security|protection|awareness|pulse|water|leak/i],
    ['smart-lock', /lock|entry|guest|access control/i],
    ['climate-thermostat', /climate|thermostat|comfort|air quality/i],
    ['lighting-bulb', /lighting|ambience|evening|night|bulb/i],
    ['music-note', /entertain|audio|cinema|music/i],
    ['installation-tools', /install|setup/i],
    ['support-headset', /support|help|caregiver|senior|aging|nursing/i],
    ['faq-chat', /faq|question/i],
    ['calendar', /guide|turnover|schedule|plan/i],
    ['location-pin', /commercial|office|property|location|rental|str /i],
    ['phone', /contact|consultation/i],
    ['concierge-bell', /concierge|bundle/i]
  ];
  return rules.find(([,pattern])=>pattern.test(title))?.[0] || 'automation-home-gear';
}

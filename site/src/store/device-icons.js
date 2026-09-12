const shapes={
 hub:['M9 14h30v22H9z M14 36v3m20-3v3','M15 22h18 M16 28h1m6 0h1m6 0h1'],
 bridge:['M6 19h15v15H6z M27 19h15v15H27z','M21 26h6 M11 24h5m-5 5h5m16-5h5m-5 5h5'],
 wifi:['M8 20a23 23 0 0 1 32 0 M13 26a16 16 0 0 1 22 0','M19 32a7 7 0 0 1 10 0 M24 38h.01'],
 lock:['M12 22h24v19H12z M17 22v-8a7 7 0 0 1 14 0v8','M24 29v6'],
 garage:['M6 21 24 7l18 14 M10 18v23h28V18','M15 25h18m-18 6h18m-18 6h18'],
 contact:['M11 7h15v34H11z M32 12h6v20h-6z','M18 15h1m-1 18h1'],
 doorbell:['M15 5h18v38H15z','M24 16a3 3 0 1 0 0 .1 M24 32a5 5 0 1 0 0 .1'],
 keypad:['M13 5h22v38H13z','M19 13h1m8 0h1m-10 7h1m8 0h1m-10 7h1m8 0h1 M20 35h8'],
 bulb:['M17 32c0-7-5-8-5-15a12 12 0 0 1 24 0c0 7-5 8-5 15z M18 37h12m-10 5h8','M21 29v-7l-3-4m9 11v-7l3-4'],
 switch:['M13 5h22v38H13z M19 13h10v23H19z','M20 21h8'],
 plug:['M13 19h22v10a11 11 0 0 1-22 0z M18 19V8m12 11V8','M24 40v5 M18 26h12'],
 outlet:['M12 5h24v38H12z M17 12h14v24H17z','M21 18v4m6-4v4 M22 29h4'],
 lamp:['M12 24 17 8h14l5 16z M24 24v15 M15 40h18','M13 25h22'],
 pendant:['M24 4v12 M11 32a13 16 0 0 1 26 0z','M12 33h24 M20 38h8'],
 sconce:['M15 12h18v25H15z M20 7h8v5m-4 25v5','M20 17h8m-8 6h8m-8 6h8'],
 spotlight:['M11 15 31 8l6 13-20 8z M16 28l-4 13h13','M35 6l4-4m1 12h6m-7 9 5 4'],
 shades:['M8 8h32v6H8z M11 14v24h26V14','M12 21h24m-24 7h24m-24 7h24 M41 15v23'],
 thermostat:['M24 5a19 19 0 1 0 0 38 19 19 0 1 0 0-38','M17 18h14l-8 15 M32 14h.01'],
 temperature:['M20 28V11a4 4 0 0 1 8 0v17a9 9 0 1 1-8 0','M24 18v15 M33 14h5m-5 7h5'],
 humidity:['M24 5S9 24 9 31a15 15 0 0 0 30 0C39 24 24 5 24 5z','M17 32c0 5 3 7 7 7'],
 camera:['M7 13h34v23H7z M12 8h10l3 5','M24 17a8 8 0 1 0 0 16 8 8 0 1 0 0-16 M34 18h1'],
 motion:['M18 13h12v25H18z M22 19h4','M11 15a17 17 0 0 0 0 21 M37 15a17 17 0 0 1 0 21 M6 9a26 26 0 0 0 0 33 M42 9a26 26 0 0 1 0 33'],
 leak:['M24 6S13 20 13 26a11 11 0 0 0 22 0C35 20 24 6 24 6z','M7 40c5-4 10 4 15 0s10 4 19 0 M19 27c0 3 2 5 5 5'],
 valve:['M5 22h14v-5h10v5h14v12H29v5H19v-5H5z','M24 17V9 M14 9h20 M24 22v12'],
 tv:['M5 9h38v26H5z M24 35v7 M15 42h18','M9 13h30v18H9z'],
 speaker:['M14 6h20v36H14z','M24 12a3 3 0 1 0 0 6 3 3 0 1 0 0-6 M24 25a6 6 0 1 0 0 12 6 6 0 1 0 0-12'],
 streaming:['M12 9h24v29H12z M18 38v5h12v-5','M20 17 29 24l-9 7z'],
 vacuum:['M24 7a18 18 0 1 0 0 36 18 18 0 1 0 0-36','M16 12h16v8H16z M10 29h28 M21 36h6'],
 appliance:['M10 13h28v27H10z M14 8h20v5 M38 21h5v10h-5','M16 20h16v13H16z M21 6V3m6 3V3'],
 home:['M5 23 24 6l19 17 M10 20v22h28V20','M20 42V29h8v13 M15 24h3m12 0h3'],
 heart:['M24 40 7 23C-1 11 14 3 24 15 34 3 49 11 41 23z','M24 40 41 23'],
 cart:['M6 8h6l5 24h21l5-17H14 M20 39h.1 M35 39h.1','M20 20h16 M23 26h10']
};
export function deviceIcon(type='home',className='device-icon') {
 const [base,accent]=shapes[type]||shapes.home;
 return `<svg class="${className}" viewBox="0 0 48 48" fill="none" aria-hidden="true" focusable="false"><path d="${base}" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><path class="icon-accent" d="${accent}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
}

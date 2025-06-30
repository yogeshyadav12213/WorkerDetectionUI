// const createMouseElement = (className, styles, duration) => {
//     const el = document.createElement('div');
//     el.className = className;
//     Object.assign(el.style, styles);
//     document.body.appendChild(el);
//     setTimeout(() => el.remove(), duration);
// };
//
// document.addEventListener('mousemove', e => createMouseElement(
//     'mouse-scanner',
//     {
//         left: (e.clientX - 10) + 'px',
//         top: (e.clientY - 10) + 'px'
//     },
//     300
// ));
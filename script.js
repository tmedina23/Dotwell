let isMouseDown = false;
let tool = 'Pencil';
let colorPicker = null;

window.onload = () => {
        initDots();
        window.addEventListener('mousedown', () => isMouseDown = true);
        window.addEventListener('mouseup', () => isMouseDown = false);
        colorPicker = document.querySelector('.colorPicker');
        initButtons();
};

initDots = () => {
    const container = document.querySelector('.container');
    for (let i = 0; i < 64 * 32; i++) {
        const dot = document.createElement('div');
        dot.classList.add('dot');
        dot.innerHTML = '•';
        dot.style.color = 'rgb(66, 66, 66)';
        container.appendChild(dot);
        dot.addEventListener('mouseenter', dotHover);
        dot.addEventListener('mousedown', dotClick);
    }
};

dotHover = (e) => {
    if (isMouseDown) {
        const dot = e.target;
        if(tool === 'Pencil'){
            dot.style.color = colorPicker.value;
        } else if (tool === 'Eraser') {
            dot.style.color = 'rgb(66, 66, 66)';
        }
    }
};

dotClick = (e) => {
    const dot = e.target;
    if(tool === 'Pencil'){
        dot.style.color = colorPicker.value;
    } else if (tool === 'Eraser') {
        dot.style.color = 'rgb(66, 66, 66)';
    }
};

initButtons = () => {
    const tools = document.querySelectorAll('.tool');
    const clearButton = document.querySelector('.clear');
    tools.forEach(t => {
        t.addEventListener('click', () => {
            tools.forEach(t => t.classList.remove('active'));
            t.classList.add('active');
            tool = t.innerHTML;
            console.log(tool);
        });
    });
    clearButton.addEventListener('click', () => {
        const dots = document.querySelectorAll('.dot');
        dots.forEach(dot => dot.style.color = 'rgb(66, 66, 66)');
    });
};

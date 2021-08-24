document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function () {
            newFunction(button);
        }
    });
});

function newFunction(button) {
    document.querySelector('#fligts_header').style.color = button.dataset.color;
}
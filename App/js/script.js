const canvas = document.getElementById('whiteboard');
const ctx = canvas.getContext('2d');

let drawing = false;

canvas.addEventListener('mousedown', () => {
    drawing = true;
});

canvas.addEventListener('mouseup', () => {
    drawing = false;
    ctx.beginPath();
});

canvas.addEventListener('mousemove', draw);

function draw(event) {
    if (!drawing) return;
    ctx.lineWidth = document.getElementById('brushSize').value;
    ctx.lineCap = 'round';

    ctx.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
}

document.getElementById('colorPicker').addEventListener('change', (event) => {
    ctx.strokeStyle = event.target.value;
});

document.getElementById('brushSize').addEventListener('input', (event) => {
    document.getElementById('brushSizeDisplay').textContent = event.target.value;
});

document.getElementById('eraser').addEventListener('click', clearCanvas);

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}


// 以下内容为关于调用摄像头的代码
document.addEventListener('DOMContentLoaded', function() {
    // 设置视频约束条件
    const constraints = {
        video: true//这里表示需要获取视频流
    };

    // 获取视频元素并将其赋值给“video”
    const video = document.getElementById('video');

    function handleSuccess(stream) {
        // 当成功获取到媒体流时，将其设置为视频元素的源
        video.srcObject = stream;
    }

    function handleError(error) {
        // 输出错误信息
        console.error('getUserMedia error: ', error);
    }

    // 请求用户媒体设备
    navigator.mediaDevices.getUserMedia(constraints).then(handleSuccess).catch(handleError);

    // 点击视频时，截取一帧并上传到服务器
    video.addEventListener('click', function() {
        const canvas = document.createElement('canvas');
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext('2d').drawImage(video, 0, 0);
        let imageData = canvas.toDataURL('image/jpeg');

        // 通过fetch API发送截图数据到服务器
        fetch('/process_image', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                image_data: imageData
            })
        });
    });
});

//以下是关于日历日程的部分，目前还没做好
// function updateCalendar() {
//     // ... [other code]
//
//     for (let i = 1; i <= lastDay.getDate(); i++) {
//         daysStr += `<div class="day">${i}`;
//
//         // Check if there are any tasks for this date
//         const tasksForThisDate = document.querySelectorAll(`.task[data-start-date<="${i}"][data-end-date>="${i}"]`);
//         tasksForThisDate.forEach(task => {
//             daysStr += task.outerHTML;
//         });
//
//         daysStr += `</div>`;
//     }
//
//     // ... [other code]
// }

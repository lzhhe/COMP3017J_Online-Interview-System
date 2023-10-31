// 以下的内容是用于绘制白板，使用了canvas来实现
// 获取画布元素和其2D渲染上下文
const canvas = document.getElementById('whiteboard');
const ctx = canvas.getContext('2d');

// 设置一个布尔值变量“drawing”来判断是否正在进行绘图
let drawing = false;

// 使用canvas相关函数检索鼠标状态，当鼠标左键按下时，设置绘图为true
canvas.addEventListener('mousedown', () => drawing = true);

// 当鼠标左键抬起时，设置绘图为false并开始一个新的路径
canvas.addEventListener('mouseup', () => {
    drawing = false;
    ctx.beginPath();
});

// 鼠标按下时移动时进行绘图
canvas.addEventListener('mousemove', draw);

function draw(event) {
    // 如果不在绘图状态，则不执行绘图操作，根据drawing的值来进行判断
    if (!drawing) return;
    // TODO：设置线宽和线的端点样式（目前还是默认值，之后可以考虑加入组件控制线条宽度和样式）
    ctx.lineWidth = 5;
    ctx.lineCap = 'round';
    // 获取颜色选择器的值作为线条颜色
    ctx.strokeStyle = document.getElementById('colorPicker').value;
    // 绘制线条
    ctx.lineTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(event.clientX - canvas.offsetLeft, event.clientY - canvas.offsetTop);
}
// 这里获取colorPicker的颜色变化，当颜色选择器的值改变时，更新线条颜色
document.getElementById('colorPicker').addEventListener('change', (event) => {
    ctx.strokeStyle = event.target.value;
});


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

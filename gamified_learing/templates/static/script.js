const statusText = document.getElementById("status");

const video = document.createElement("video");
video.autoplay = true;
video.style.width = "400px";

document.body.appendChild(video);

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
    statusText.innerText = "Camera started ✅";
  })
  .catch(err => {
    console.error(err);
    statusText.innerText = "Camera error ❌";
    alert("Camera access failed");
  });

var canvas = document.getElementById('preview-canvas'),
context = canvas.getContext('2d');
let fileInput = document.getElementById('upload');

var inital_image;

function handleImageUpload() 
{
    var image = document.getElementById("upload").files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
     // document.getElementById("preview-image").src = e.target.result;
        base_image = new Image();
        base_image.src = e.target.result;
        base_image.onload = function(){

            context.drawImage(base_image, 0, 0, base_image.width,    base_image.height,     // source rectangle
                                          0, 0, canvas.width, canvas.height);
            inital_image = base_image
        }
    }
    reader.readAsDataURL(image);

} 

var current_brightness=0;
var current_contrast=0;

function changeBrightness()
{
    current_brightness = document.getElementById("brightnessSlider").value;
    Caman("#preview-canvas", function () {
        // manipulate image here
        this.revert(false);
        this.contrast(current_contrast);
        this.brightness(current_brightness).render();
    });
}
function changeContrast()
{
    current_contrast = parseInt(document.getElementById("contrastSlider").value);
    Caman("#preview-canvas", function () {
        // manipulate image here
        this.revert(false);
        this.brightness(current_brightness);
        this.contrast(current_contrast).render();
    });
}
function sendProcessed(){
    document.getElementById('upload').value = canvas.toDataURL('image/jpeg');
    document.getElementById("fileForm").submit();

}
<!DOCTYPE html>
<html>
    <head>
        <title>VISOR</title>
        <script src="lib\require.js"></script>
        <script src="lib\CamanJS\caman.full.js"></script>
    </head>
    <body>
        <form id= "fileForm" action="TTR.php" method="post" enctype="multipart/form-data">
            <p id="uploadText">Select image to upload:</p>
            <input id="upload" type="file" name="TTR_file" onChange="handleImageUpload()" />
            <input type="radio" id="TTR_pnm" name="testToRun" value="pnm">
            <input type="hidden" name="fileToUpload" id="fileToUpload"/>
            <label for="pneumonia">Pneumonia</label><br>
        </form>
        <canvas id="preview-canvas" width="300" height="300"></canvas>

        <p>brightness</p>
        <input id="brightnessSlider" type="range" min="-100" max="100" step="1" value="0" data-filter="brightness"  onChange="changeBrightness()">
        <span id="brightnessText">0</span>
        <br>
        <p>contrast</p>
        <input id="contrastSlider" type="range" min="-100" max="100"  step="1" value="0" data-filter="contrast" onChange="changeContrast()">
        <span id="contrastText">0</span>
        <br>

        <button onClick="sendProcessed()"> RUN ANALYZER</button>

        <script src="script.js"></script>
    </body>
</html>

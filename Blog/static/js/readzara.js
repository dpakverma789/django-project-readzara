

function fileValidation(){
    const extension_set = ['jpg', 'jpeg', 'png'];
    let fileInput = document.getElementById('post_image');
    let fileName = fileInput.value;
    let extension = fileName.substring(fileName.lastIndexOf('.') + 1);
    if (!extension_set.includes(extension)){
        alert("Required Image For your Post!");
        fileInput.value = '';
        return false;
    }
    return true;
}
function sub(obj)
{
   var file = obj.value;
   var fileName = file.split("\\");
   document.getElementById("customized").innerHTML = fileName[fileName.length - 1];
   event.preventDefault();
}

function updateCSS() {
   $.ajax({
      url: "/uploader",
      method: "GET",
      success: function(data) {
         $("#window").css("background-color", data.color);
         $("#neutral").css("display", data.neutral);
         $("#IDC").css("display", data.idc);
         $("#nonIDC").css("display", data.nonidc);
         $("#accuracy").text(data.acc)
         console.log(data)
      }
   });
}

function show_indicator() {
  document.getElementById("loading").style.display = "block";
  document.getElementById("content").style.display = "none";
}

const fileInputs = document.querySelectorAll('input[type=file]');
const btnUploadBuilding = document.getElementById('btn_upload_building');
const btnUploadPolygon = document.getElementById('btn_upload_polygon');
const uploadObjectForm = document.getElementById('form_upload_object');

uploadObjectForm.addEventListener('submit', function (event) {
  const input = document.getElementById('building_id');

  if (!input.value) {
    alert("건물 아이디를 입력하세요.");
    input.focus();
    event.preventDefault();
  } else {
    show_indicator();
  }
});


fileInputs.forEach(e => {
  e.addEventListener('change', e => {
    const selectedFiles = [...e.target.files];

    let nextSibling = e.target.nextElementSibling;
    if (nextSibling) nextSibling.disabled = false;
  });
})

btnUploadBuilding.addEventListener('click', e => {
  show_indicator();
})

btnUploadPolygon.addEventListener('click', e => {
  show_indicator();
})

const btnDeleteObject = document.getElementsByClassName("delete-object")
for (const btn of btnDeleteObject) {
  btn.addEventListener('click', e => {
    if (confirm('삭제하시겠습니까?')) {
      show_indicator();
    } else {
      e.preventDefault();
    }
  })
}
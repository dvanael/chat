
document.addEventListener("htmx:wsAfterSend", function(evt) {
  const form = document.querySelector("#id-form-message");
  if (form) {
      form.reset();
  }
});
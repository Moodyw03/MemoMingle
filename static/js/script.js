"use strict";

// display the success and error messages for a short time

const success = document.getElementById("success");
const error = document.getElementById("error");

function removeParam(param) {
  const url = window.location.href;
  const urlParams = new URLSearchParams(url);
  urlParams.delete(param);
  window.history.replaceState({}, "", window.location.pathname);
}

if (success) {
  setTimeout(() => {
    success.style.display = "none";

    // remove the success message from the url
    removeParam("success");
  }, 3000);
}

if (error) {
  setTimeout(() => {
    error.style.display = "none";

    // remove the error message from the url
    removeParam("error");
  }, 3000);
}

// Check if the both passwords are the same
function checkPasswords() {
  var password = document.getElementById("password").value;
  var confirmPassword = document.getElementById("confirm-password").value;

  if (password !== confirmPassword) {
    alert("Passwords do not match.");
    return false; // Prevent form submission
  }
  return true;
}

// Check if the both passwords are the same for profile update
function checkPasswordsProfile() {
  var newPassword = document.getElementById("new-password").value;
  var confirmNewPassword = document.getElementById(
    "confirm-new-password"
  ).value;

  if (newPassword !== confirmNewPassword) {
    alert("New passwords do not match.");
    return false; // Prevent form submission
  }
  return true;
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("modal-btn"); // Make sure you have a button with this ID in your HTML

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// Get the button element that closes the modal
var cancel = document.getElementById("cancel");

// When the user clicks on the button, open the modal
btn.onclick = function () {
  modal.style.display = "block";
};

// When the user clicks on cancel, close the modal
cancel.onclick = function () {
  modal.style.display = "none";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
  modal.style.display = "none";
};

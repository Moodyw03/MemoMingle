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
  const newPassword = document.getElementById("new-password").value;
  const confirmPassword = document.getElementById("confirm-new-password").value;

  if (newPassword !== confirmPassword) {
    alert("New passwords do not match!");
    return false;
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

// Session timeout management
document.addEventListener("DOMContentLoaded", () => {
  // Constants for session timeout (in milliseconds)
  const WARNING_TIME = 60000; // 1 minute warning before timeout
  const CHECK_INTERVAL = 10000; // Check every 10 seconds

  // Get session timeout value (set in backend based on device type)
  // Default to 30 minutes if not specified
  const SESSION_TIMEOUT = 30 * 60 * 1000; // 30 minutes

  let lastActivity = new Date().getTime();
  let warningDisplayed = false;
  let countdownTimer = null;
  let sessionCheckTimer = null;

  // DOM elements for warning modal
  const warningModal = document.getElementById("sessionWarningOverlay");
  const countdownElement = document.getElementById("sessionCountdown");
  const continueButton = document.getElementById("continueSessionBtn");
  const logoutButton = document.getElementById("logoutNowBtn");

  // Skip if we're not on a page with the session warning overlay
  if (!warningModal) return;

  // Activity events to monitor
  const activityEvents = [
    "mousedown",
    "mousemove",
    "keypress",
    "scroll",
    "touchstart",
    "click",
    "keydown",
  ];

  // Function to update last activity timestamp
  function updateActivity() {
    lastActivity = new Date().getTime();

    // If warning is displayed, hide it and reset
    if (warningDisplayed) {
      hideWarning();
    }
  }

  // Add all activity event listeners
  activityEvents.forEach((event) => {
    document.addEventListener(event, updateActivity, { passive: true });
  });

  // Function to check session status
  function checkSession() {
    const currentTime = new Date().getTime();
    const inactiveTime = currentTime - lastActivity;

    // If inactive time exceeds timeout minus warning time, show warning
    if (inactiveTime > SESSION_TIMEOUT - WARNING_TIME && !warningDisplayed) {
      showWarning();
    }
  }

  // Function to show the warning modal
  function showWarning() {
    warningDisplayed = true;
    warningModal.classList.add("active");

    // Start countdown
    let secondsLeft = WARNING_TIME / 1000;
    updateCountdown(secondsLeft);

    countdownTimer = setInterval(() => {
      secondsLeft--;
      updateCountdown(secondsLeft);

      // When countdown reaches 0, log the user out
      if (secondsLeft <= 0) {
        logoutUser();
      }
    }, 1000);
  }

  // Function to hide the warning modal
  function hideWarning() {
    warningDisplayed = false;
    warningModal.classList.remove("active");

    // Clear the countdown interval
    if (countdownTimer) {
      clearInterval(countdownTimer);
      countdownTimer = null;
    }
  }

  // Function to update the countdown display
  function updateCountdown(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    countdownElement.textContent = `${minutes}:${
      remainingSeconds < 10 ? "0" : ""
    }${remainingSeconds}`;
  }

  // Function to log the user out
  function logoutUser() {
    // Clear timers
    clearInterval(countdownTimer);
    clearInterval(sessionCheckTimer);

    // Redirect to logout route
    window.location.href = "/sign-out";
  }

  // Event listeners for the warning modal buttons
  if (continueButton) {
    continueButton.addEventListener("click", updateActivity);
  }

  if (logoutButton) {
    logoutButton.addEventListener("click", logoutUser);
  }

  // Start checking session status
  sessionCheckTimer = setInterval(checkSession, CHECK_INTERVAL);

  // Initial activity timestamp
  updateActivity();
});

// Emoji selector functionality for note editing
document.addEventListener("DOMContentLoaded", () => {
  // Common emoji selections for kids
  const emojis = [
    "😀",
    "",
    "😂",
    "🤣",
    "😃",
    "😄",
    "😅",
    "😆",
    "😊",
    "",
    "😎",
    "😍",
    "🥰",
    "😗",
    "😙",
    "😚",
    "🙂",
    "🤗",
    "🤩",
    "🤔",
    "🤨",
    "😐",
    "😑",
    "😶",
    "🙄",
    "😏",
    "😣",
    "😥",
    "😮",
    "🤐",
    "😯",
    "😪",
    "😫",
    "🥱",
    "😴",
    "😌",
    "😛",
    "😜",
    "😝",
    "🤤",
    "😒",
    "😓",
    "😔",
    "😕",
    "🙃",
    "🤑",
    "😲",
    "☹️",
    "🙁",
    "",
    "😞",
    "😟",
    "😤",
    "😢",
    "😭",
    "😦",
    "😧",
    "",
    "😩",
    "🤯",
    "😬",
    "😰",
    "😱",
    "🥵",
    "🥶",
    "😳",
    "🤪",
    "😵",
    "🥴",
    "😠",
    "😡",
    "🤬",
    "😷",
    "🤒",
    "🤕",
    "🤢",
    "🤮",
    "🤧",
    "😇",
    "🥳",
    "🥺",
    "🤠",
    "🤡",
    "🤥",
    "🤫",
    "🤭",
    "🧐",
    "🤓",
    "😈",
    "👻",
    "👽",
    "👾",
    "🤖",
    "💩",
    "🎃",
    "🧙",
    "🐶",
    "🐱",
    "🐭",
    "🐹",
    "🐰",
    "🦊",
    "🐻",
    "🐼",
  ];

  // Create emoji picker if on note edit page
  const noteTextarea = document.querySelector(".note__edit--textarea");
  if (noteTextarea) {
    // Create emoji selector container
    const emojiSelector = document.createElement("div");
    emojiSelector.className = "emoji-selector";

    // Create emoji button
    const emojiButton = document.createElement("button");
    emojiButton.className = "emoji-button";
    emojiButton.type = "button";
    emojiButton.innerHTML = "😊";
    emojiButton.setAttribute("title", "Insert emoji");

    // Create emoji dropdown
    const emojiDropdown = document.createElement("div");
    emojiDropdown.className = "emoji-dropdown";

    // Add emojis to dropdown
    emojis.forEach((emoji) => {
      const emojiItem = document.createElement("div");
      emojiItem.className = "emoji-item";
      emojiItem.innerHTML = emoji;
      emojiItem.addEventListener("click", () => {
        // Insert emoji at cursor position
        const cursorPos = noteTextarea.selectionStart;
        const textBefore = noteTextarea.value.substring(0, cursorPos);
        const textAfter = noteTextarea.value.substring(cursorPos);
        noteTextarea.value = textBefore + emoji + textAfter;

        // Update cursor position
        const newCursorPos = cursorPos + emoji.length;
        noteTextarea.setSelectionRange(newCursorPos, newCursorPos);
        noteTextarea.focus();

        // Close dropdown
        emojiDropdown.classList.remove("open");
      });
      emojiDropdown.appendChild(emojiItem);
    });

    // Toggle dropdown on button click
    emojiButton.addEventListener("click", (e) => {
      e.preventDefault();
      emojiDropdown.classList.toggle("open");
    });

    // Close dropdown when clicking outside
    document.addEventListener("click", (e) => {
      if (!emojiSelector.contains(e.target)) {
        emojiDropdown.classList.remove("open");
      }
    });

    // Add button and dropdown to selector
    emojiSelector.appendChild(emojiButton);
    emojiSelector.appendChild(emojiDropdown);

    // Insert selector before textarea
    const formGroup = noteTextarea.parentElement;
    formGroup.insertBefore(emojiSelector, noteTextarea);
  }
});

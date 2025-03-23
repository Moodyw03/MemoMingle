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

// Content filtering for preventing inappropriate input
document.addEventListener("DOMContentLoaded", () => {
  // Import the inappropriate words list from our filter
  // This is a simplified version of the server-side list
  const inappropriateWords = [
    // Common profanity
    "shit",
    "fuck",
    "damn",
    "hell",
    "ass",
    "bitch",
    "crap",
    "piss",
    "dick",
    "cock",
    "pussy",
    "asshole",
    "bastard",
    "motherfucker",
    "bullshit",
    "horseshit",
    "jackass",
    "cunt",
    "twat",
    "whore",
    "slut",
    "hoe",
    "tits",
    "boobs",
    "wanker",
    "douchebag",
    "douche",
    "jerk",
    "jerkoff",
    "dumbass",
    "fag",
    "faggot",
    "homo",
    "queer",
    "retard",
    "retarded",
    "nigger",
    "nigga",
    "spic",
    "wetback",
    "chink",
    "gook",
    "kike",
    "paki",
    "dyke",
    "kyke",
    "raghead",
    "negro",

    // Partial matches
    "f*ck",
    "f**k",
    "f***",
    "s***",
    "sh*t",
    "b*tch",
    "a**",
    "a**hole",
    "a-hole",
    "bs",
    "b.s.",
    "wtf",
    "stfu",
    "fu",
    "sob",
    "pos",
    "mofo",
    "mf",
    "mtf",
    "ftm",
    "lmfao",
    "lmao",

    // Sexual terms
    "porn",
    "blowjob",
    "handjob",
    "rimjob",
    "anal",
    "cum",
    "cumming",
    "jizz",
    "masturbate",
    "dildo",
    "vibrator",
    "sex",
    "sexy",
    "orgasm",
    "boner",
    "erection",
    "horny",

    // Drug-related
    "weed",
    "cocaine",
    "heroin",
    "meth",
    "crack",
    "lsd",
    "ecstasy",
    "marijuana",
    "pot",
    "dope",
    "high",
    "stoned",
    "junkie",
  ];

  // Create a message container for warnings
  let messageContainer = null;

  function createMessageContainer() {
    if (messageContainer) return messageContainer;

    messageContainer = document.createElement("div");
    messageContainer.className = "inappropriate-language-warning";
    messageContainer.style.display = "none";
    messageContainer.style.position = "fixed";
    messageContainer.style.bottom = "20px";
    messageContainer.style.right = "20px";
    messageContainer.style.backgroundColor = "#ff6b6b";
    messageContainer.style.color = "white";
    messageContainer.style.padding = "12px 20px";
    messageContainer.style.borderRadius = "8px";
    messageContainer.style.boxShadow = "0 4px 12px rgba(0,0,0,0.15)";
    messageContainer.style.zIndex = "9999";
    messageContainer.style.fontWeight = "bold";
    messageContainer.style.fontSize = "14px";
    messageContainer.style.transition = "opacity 0.3s ease";

    document.body.appendChild(messageContainer);
    return messageContainer;
  }

  function showInappropriateLanguageWarning(word) {
    const container = createMessageContainer();
    container.textContent = `⚠️ Please use child-friendly language. The word "${word}" is not allowed.`;
    container.style.display = "block";
    container.style.opacity = "1";

    // Hide after 3 seconds
    setTimeout(() => {
      container.style.opacity = "0";
      setTimeout(() => {
        container.style.display = "none";
      }, 300);
    }, 3000);
  }

  // Function to detect inappropriate words in a string
  function containsInappropriateWord(text) {
    if (!text) return false;

    const textLower = text.toLowerCase();

    for (const word of inappropriateWords) {
      // Check for whole words using regex
      const pattern = new RegExp(`\\b${word}\\b`, "i");
      if (pattern.test(textLower)) {
        return word;
      }

      // Also check if the word is contained anywhere
      if (textLower.includes(word)) {
        return word;
      }
    }

    return false;
  }

  // Function to prevent entering inappropriate words
  function preventInappropriateInput(event) {
    const input = event.target;
    const currentValue = input.value;

    // Check what the text would be after this key press
    const newChar = event.key;
    if (newChar.length === 1 || newChar === "Space") {
      // For regular key presses, check if adding this character would create a bad word
      const potentialValue =
        currentValue + (newChar === "Space" ? " " : newChar);
      const badWord = containsInappropriateWord(potentialValue);

      if (badWord) {
        event.preventDefault();
        showInappropriateLanguageWarning(badWord);
        return false;
      }
    }

    return true;
  }

  // Function to check pasted content
  function checkPastedContent(event) {
    // Get pasted content
    const clipboardData = event.clipboardData || window.clipboardData;
    const pastedText = clipboardData.getData("text");

    // Check if the pasted content contains inappropriate words
    const badWord = containsInappropriateWord(pastedText);
    if (badWord) {
      event.preventDefault();
      showInappropriateLanguageWarning(badWord);
      return false;
    }

    return true;
  }

  // Apply the filters to note title and content fields
  const noteTitle = document.querySelector('input[name="title"]');
  const noteContent = document.querySelector('textarea[name="content"]');

  if (noteTitle) {
    noteTitle.addEventListener("keypress", preventInappropriateInput);
    noteTitle.addEventListener("paste", checkPastedContent);
  }

  if (noteContent) {
    noteContent.addEventListener("keypress", preventInappropriateInput);
    noteContent.addEventListener("paste", checkPastedContent);
  }

  // Check the input whenever it changes (for cases like auto-complete)
  function checkInputContent(event) {
    const input = event.target;
    const currentValue = input.value;

    // Check for inappropriate words
    for (const word of inappropriateWords) {
      // Create pattern that can detect the word with word boundaries
      const boundaryPattern = new RegExp(`\\b${word}\\b`, "gi");

      // Also check for words embedded within other text
      const containsPattern = new RegExp(word, "gi");

      // First try to remove whole words
      if (boundaryPattern.test(currentValue)) {
        // Remove the bad word completely (replace with empty string)
        input.value = currentValue.replace(boundaryPattern, "");
        showInappropriateLanguageWarning(word);

        // Re-check the input in case there are multiple instances
        setTimeout(() => checkInputContent(event), 10);
        return;
      }

      // Then check if the word is contained anywhere
      if (containsPattern.test(currentValue)) {
        // Remove the bad word completely (replace with empty string)
        input.value = currentValue.replace(containsPattern, "");
        showInappropriateLanguageWarning(word);

        // Re-check the input in case there are multiple instances
        setTimeout(() => checkInputContent(event), 10);
        return;
      }
    }
  }

  if (noteTitle) {
    noteTitle.addEventListener("input", checkInputContent);
  }

  if (noteContent) {
    noteContent.addEventListener("input", checkInputContent);
  }
});

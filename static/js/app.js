// Toasts a default alert
function toastAlert() {
    var alertContent = "This is a default alert with <a href='#' class='alert-link'>a link</a> being toasted.";
    // Built-in function
    halfmoon.initStickyAlert({
        content: alertContent, // Required, main content of the alert, type: string (can contain HTML)
        title: "Default alert" // Optional, title of the alert, default: "", type: string
    })
}

// Toasts another alert (here, the options are shown)
function toastAnotherAlert() {
    var alertContent = "This is another alert with <a href='#' class='alert-link'>a link</a> being toasted.";
    // Built-in function
    halfmoon.initStickyAlert({
        content: alertContent, // Required, main content of the alert, type: string (can contain HTML)
        title: "Another alert", // Optional, title of the alert, default: "", type: string
        alertType: "", // Optional, type of the alert, default: "", must be "alert-primary" || "alert-success" || "alert-secondary" || "alert-danger"
        fillType: "", // Optional, fill type of the alert, default: "", must be "filled-lm" || "filled-dm" || "filled"
        hasDismissButton: true, // Optional, the alert will contain the close button if true, default: true, type: boolean
        timeShown: 5000 // Optional, time the alert stays on the screen (in ms), default: 5000, type: number
    })
}
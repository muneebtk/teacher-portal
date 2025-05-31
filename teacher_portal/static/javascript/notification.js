function showError(message) {
    createNotification(message, 'error');
}

function showSuccess(message) {
    createNotification(message, 'success');
}

function createNotification(message, type) {
    // Create the notification container if it doesn't exist
    let notificationContainer = document.getElementById('notification-container');
    if (!notificationContainer) {
        notificationContainer = document.createElement('div');
        notificationContainer.id = 'notification-container';
        notificationContainer.style.position = 'fixed';
        notificationContainer.style.top = '20px';
        notificationContainer.style.right = '20px';
        notificationContainer.style.zIndex = '9999';
        document.body.appendChild(notificationContainer);
    }

    // Create the notification
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;

    // Apply styles
    notification.style.padding = '10px 20px';
    notification.style.marginBottom = '10px';
    notification.style.borderRadius = '5px';
    notification.style.color = '#fff';
    notification.style.fontSize = '14px';
    notification.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
    notification.style.transition = 'opacity 0.3s ease';

    // Specific styles for error and success
    if (type === 'error') {
        notification.style.backgroundColor = '#e74c3c'; // Red
    } else if (type === 'success') {
        notification.style.backgroundColor = '#2ecc71'; // Green
    }

    // Add the notification to the container
    notificationContainer.appendChild(notification);

    // Automatically remove the notification after 3 seconds
    setTimeout(() => {
        notification.style.opacity = '0'; // Fade out
        setTimeout(() => notification.remove(), 300); // Remove from DOM after fade-out
    }, 3000);
}

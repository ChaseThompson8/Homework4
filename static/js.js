$(document).ready(function () {
    // Dom content is loaded

    $('#complete').click(completed);
    $('#confirmDelete').click(deleted);

    function completed() {
        $('#complete').remove();
        $('#task').each(function() {
            $(this).replaceWith($('<strike>' + this.innerHTML + '</strike>'));
        });
    }

    function deleted() {
        $('#text').html({{ task.description }} + "was removed");
    }
}

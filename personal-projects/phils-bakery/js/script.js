let navDropDownOpen = false;

$('#navigation__dropdown-icon').click(function () {
    if (navDropDownOpen) {
        $('#navigation__dropdown').removeClass('openDropDown');
        navDropDownOpen = false;
    } else {
        $('#navigation__dropdown').addClass('openDropDown');
        navDropDownOpen = true;
    }
});
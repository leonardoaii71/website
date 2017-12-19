
$(document).ready(function(){
    var $myForm = $('#vehiculoForm')
    $myForm.submit(function(event){
        event.preventDefault()
        console.log("dentro")
        var $formData = $(this).serialize()
        var $thisURL = $myForm.attr('data-url')
        $.ajax({
            method: "POST",
            url: $thisURL,
            data: $formData,
            success: handleFormSuccess,
            error: handleFormError,
        })
    })

    function handleFormSuccess(data, textStatus, jqXHR){
        console.log(data)
        console.log(textStatus)
        console.log(jqXHR)
        $('#id_vehiculo').val(data.message)
        $('#id_vehiculo').attr('placeholder', data.desc)

        $myForm[0].reset(); // reset form data
    }

    function handleFormError(jqXHR, textStatus, errorThrown){
        console.log(jqXHR)
        console.log(textStatus)
        console.log(errorThrown)
    }
})
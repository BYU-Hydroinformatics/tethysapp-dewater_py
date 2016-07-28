
//  ################################# UTILITIES ############################################
//
//  This file is used for general purpose functions associated with model dialogs.
//	It requires some associated HTML to be placed in the *.html files from which
//	the modal dialog will be used.
//
//	--Norm Jones
//
//  ########################################################################################

"use strict";

// Error message function using bootstrap
function error_message(errMessageText) {
    $('#GenericModal').on('show.bs.modal', function (event) {
    	$('#ModalTitle').text('Error Message');
        $('#ModalBody').text(errMessageText);
        $('#ModalFooter').hide();
    })
    $('#GenericModal').modal('show')
}

// Generic modal dialog using bootstrap
function modal_dialog(title, htmlBody, showFooter) {
    $('#GenericModal').on('show.bs.modal', function (event) {
        $('#ModalTitle').text(title);
        $('#ModalBody').html(htmlBody);
        // Insert equation into modal
	   	var div = document.getElementById('Equation');
		var img = new Image();
		img.src = "/static/dewater_py/images/EQN.png";
		div.appendChild(img);

        if (showFooter)
        	$('#ModalFooter').show();
        else
        	$('#ModalFooter').hide();
    })
    $('#GenericModal').modal('show')
}

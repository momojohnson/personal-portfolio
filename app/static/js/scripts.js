$(function(){
  $(".typed").typed({
  		strings: ["Java Applications.", "Python Web Applications.", " C# Applications.", "JavaScript Web Applications."],
  		// Optionally use an HTML element to grab strings from (must wrap each string in a <p>)
  		stringsElement: null,
  		// typing speed
  		typeSpeed: 40,
  		// time before typing starts
  		startDelay: 1200,
  		// backspacing speed
  		backSpeed: 30,
  		// time before backspacing
  		backDelay: 500,
  		// loop
  		loop: true,
  		// false = infinite

  		// show cursor
  		showCursor: true,
  		// character for cursor
  		cursorChar: "|",

  	});

    //Animate css
    $(".project-pic").on('mouseenter',function(){
    //alert($(this).attr('class'));
    $(this).addClass('animated bounce');
      console.log('Hover')
    });

$('.project-pic').on('mouseleave', function(){
  $(this).removeClass('animated bounce');
})

// Post contact message using ajax to avoid page refresh

$('#contact-message').on('submit', function(event){
  event.preventDefault();
  var url = $('#contact-message').attr('action');
  var request = $.ajax({
  url: url,
  method: "POST",
  // Get data from the form
  data: $('#contact-message').serialize(),
});

// Request was successful. 
request.done(function(message ) {
  // Checks for errors on forms input
  if(message.errors){
    if(message.errors.first_name){
      console.log("Please enter an email adress");
      $("#first-name strong").text(message.errors.first_name[0]);
      $("#first-name").show('fade');
      $('#first-name').on('click', function(){
        $(this).hide('fade');
      });

  }
  if(message.errors.last_name){
    $("#last-name strong").text(message.errors.last_name[0]);
    $("#last-name").show('fade');
    $("#last-name").on('click', function(){
      $(this).hide('fade');
    });
  }

  if(message.errors.email){
    $("#email strong").text(message.errors.email[0]);
    $("#email").show('fade');
    $("#email").on('click', function(){
      $(this).hide('fade');
    });
  }
  if(message.errors.phone_number){
      console.log("Please enter a phone number");
      $("#phone-number strong").text(message.errors.phone_number[0]);
      $("#phone-number").show('fade');
      $("#phone-number").on('click', function(){
        $(this).hide('fade');
      });
  }
  if(message.errors.message){
      console.log("Please enter message");
      $("#message strong").text(message.errors.message[0]);
      $("#message").show('fade');

      $("#message").on('click', function(){
        $(this).hide('fade');
      })
  }
}else{
  // The form was successfully submitted and there was no error
  $('#message-success').show('fade');
  $("#message-success").on("click", function(){
    $(this).hide('fade');
  })
}

});

// Form couldn't be submitted to the provided url
request.fail(function( jqXHR, textStatus ) {
  alert( "Request failed: " + textStatus );
});

})
// Adds material design icon to a label tag
$('#first-name label').prepend('<i class="material-icons">account_box</i>');


})

document.getElementById('emailForm').addEventListener('submit', function(event){ //This is executed when the user press send email
    event.preventDefault(); //Prevent the default behavior of submit button, for example, validate the data of the form.

    const form = event.target; // This is the element that is getting the submit action (the form).

    // get values

    const name = form.elements.name.value;
    const email = form.elements.email.value;
    const subject = form.elements.subject.value;
    const message = form.elements.message.value;

    //Now lets set your emailjs account
    //Add the Public Key this is different for all of us

    emailjs.init("atJKaNY2rUhb8AC6V");

    const params ={
        from_email: email,
        from_name: name,
        subject: subject,
        message: message
    };

    //Verify if subject is empty or not
    if (!subject){
        const result = confirm("Subject is empty. Are you sure you want to send this email?");//This returns true if the user press Ok.
        if(result === true){
            sendemail();
        }else{
            //do not send the email!
            //Note: You do not need the else, you can omit it.
        }
    }else{
        sendEmail();
    }

    //Function to send the email

    //Function to send the email

function sendEmail(){
    //Here you are using the EmailJs library to send the request (the email)
    //The First param is your service ID (you can find it in Email Services)
    // The second param is your template Id ( You can find it in email templates)
    emailjs.send("service_kcdf0z4","template_1on2pvw", params).then(function (response){
        alert("Email was successfully sent");
        from.reset();//clear inputs
    }, function(error){
        alert("Error sending email");
    });

}

});
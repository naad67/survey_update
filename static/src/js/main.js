    odoo.define('qzhub_billing.PersonalAccount', function (require) {
    "use strict";

    var core = require('web.core');
    const Dialog = require('web.Dialog');
    var _t = core._t;



    var question_id = document.getElementsByName("question_id");
    console.log("question_id", question_id)
    if (question_id.changed){
        $('.survey_all_data').on('click ', function (e) {
        let target = e.target
        if (target.classList.contains("o_survey_question_text_box")){
            var survey_data = document.getElementById("survey_data")
            survey_data.value = target.value;
            console.log('survey_data', survey_data)
        }
        })
    }

})
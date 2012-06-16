
###############################################################################
#
# SendSMS
# Sends an SMS to a specified phone number using the Twilio API.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SendSMS(Choreography):

    """
    Create a new instance of the SendSMS Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Twilio/SendSMS')


    def new_input_set(self):
        return SendSMSInputSet()

    def _make_result_set(self, result, path):
        return SendSMSResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendSMSChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SendSMS
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SendSMSInputSet(InputSet):
        """
        Set the value of the AccountSID input for this choreography. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        def set_AccountSID(self, value):
            InputSet._set_input(self, 'AccountSID', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the Body input for this choreography. ((required, string) The text of your SMS message.)
        """
        def set_Body(self, value):
            InputSet._set_input(self, 'Body', value)

        """
        Set the value of the From input for this choreography. ((required, string) The purchased Twilio phone number (or Twilio Sandbox number) to send the message from.)
        """
        def set_From(self, value):
            InputSet._set_input(self, 'From', value)

        """
        Set the value of the To input for this choreography. ((required, string) The destination phone number for the SMS message.)
        """
        def set_To(self, value):
            InputSet._set_input(self, 'To', value)


"""
A ResultSet with methods tailored to the values returned by the SendSMS choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SendSMSResultSet(ResultSet):
    pass

class SendSMSChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SendSMSResultSet(response, path)


###############################################################################
#
# ListUnsubscribe
# Remove a subscriber from a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListUnsubscribe(Choreography):

    """
    Create a new instance of the ListUnsubscribe Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListUnsubscribe')


    def new_input_set(self):
        return ListUnsubscribeInputSet()

    def _make_result_set(self, result, path):
        return ListUnsubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListUnsubscribeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListUnsubscribe
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListUnsubscribeInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Mailchimp.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the DeleteMember input for this choreography. ((optional, boolean) A flag used to completely delete the member from your list instead of just unsubscribing. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        def set_DeleteMember(self, value):
            InputSet._set_input(self, 'DeleteMember', value)

        """
        Set the value of the EmailAddress input for this choreography. ((required, string) The email address to unsubscribe.)
        """
        def set_EmailAddress(self, value):
            InputSet._set_input(self, 'EmailAddress', value)

        """
        Set the value of the ListId input for this choreography. ((required, string) The id of the list that contains the email address you want to unsubscribe.)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the SendGoodbye input for this choreography. ((optional, boolean) A flag used to send the goodbye email to the email address. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        def set_SendGoodbye(self, value):
            InputSet._set_input(self, 'SendGoodbye', value)

        """
        Set the value of the SendNotify input for this choreography. ((optional, boolean) A flag used to send the unsubscribe notification email to the address defined in the list email notification settings. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        def set_SendNotify(self, value):
            InputSet._set_input(self, 'SendNotify', value)


"""
A ResultSet with methods tailored to the values returned by the ListUnsubscribe choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListUnsubscribeResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Mailchimp. Returns the string "true" for success and "false" for failures.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListUnsubscribeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListUnsubscribeResultSet(response, path)


###############################################################################
#
# ListBatchUnsubscribe
# Unsubscribes one or more members from a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListBatchUnsubscribe(Choreography):

    """
    Create a new instance of the ListBatchUnsubscribe Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListBatchUnsubscribe')


    def new_input_set(self):
        return ListBatchUnsubscribeInputSet()

    def _make_result_set(self, result, path):
        return ListBatchUnsubscribeResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListBatchUnsubscribeChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListBatchUnsubscribe
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListBatchUnsubscribeInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Mailchimp)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the DeleteMember input for this choreography. ((optional, boolean) A flag used to completely delete the member from your list instead of just unsubscribing. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        def set_DeleteMember(self, value):
            InputSet._set_input(self, 'DeleteMember', value)

        """
        Set the value of the Email input for this choreography. ((required, string) The email address to unsubscribe from a Mailchimp list . Multiple emails can be supplied separated by commas.)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the ListId input for this choreography. ((required, string) The Mailchimp List ID)
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
        Set the value of the SupressErrors input for this choreography. ((optional, boolean) Whether or not to suppress errors that arise from attempting to unsubscribe an email address. Defaults to 0 (false). Set to 1 (true) to supress errors.)
        """
        def set_SupressErrors(self, value):
            InputSet._set_input(self, 'SupressErrors', value)


"""
A ResultSet with methods tailored to the values returned by the ListBatchUnsubscribe choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListBatchUnsubscribeResultSet(ResultSet):
        """
        Retrieve the value for the "ErrorList" output from this choreography execution. ((json) A list of emails that were not successfully unsubscribed.)
        """
        def get_ErrorList(self):
            return self._output.get('ErrorList', None)
        """
        Retrieve the value for the "SuccessList" output from this choreography execution. ((json) A list of email successfully unsubscribed.)
        """
        def get_SuccessList(self):
            return self._output.get('SuccessList', None)

class ListBatchUnsubscribeChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListBatchUnsubscribeResultSet(response, path)

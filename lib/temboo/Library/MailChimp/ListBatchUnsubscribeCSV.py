
###############################################################################
#
# ListBatchUnsubscribeCSV
# Unsubscribes one or more members listed in a CSV file from a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListBatchUnsubscribeCSV(Choreography):

    """
    Create a new instance of the ListBatchUnsubscribeCSV Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListBatchUnsubscribeCSV')


    def new_input_set(self):
        return ListBatchUnsubscribeCSVInputSet()

    def _make_result_set(self, result, path):
        return ListBatchUnsubscribeCSVResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListBatchUnsubscribeCSVChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListBatchUnsubscribeCSV
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListBatchUnsubscribeCSVInputSet(InputSet):
        """
        Set the value of the CSVFile input for this choreography. ((conditional, multiline) The list of subscriber email addresses to unsubscribe in CSV format.)
        """
        def set_CSVFile(self, value):
            InputSet._set_input(self, 'CSVFile', value)

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
        Set the value of the ListId input for this choreography. ((required, string) The id of the Mailchimp list associated with the email addresses to unsubscribe.)
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
        Set the value of the VaultFile input for this choreography. (A path to a csv file in the vault containing the email addresses to unsubscribe. Can be used as an alternative to the CSVFile input.)
        """


"""
A ResultSet with methods tailored to the values returned by the ListBatchUnsubscribeCSV choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListBatchUnsubscribeCSVResultSet(ResultSet):
        """
        Retrieve the value for the "ErrorList" output from this choreography execution. ((multiline) A list of emails that were not successfully unsubscribed.)
        """
        def get_ErrorList(self):
            return self._output.get('ErrorList', None)
        """
        Retrieve the value for the "SuccessList" output from this choreography execution. ((multiline) A list of email successfully unsubscribed.)
        """
        def get_SuccessList(self):
            return self._output.get('SuccessList', None)

class ListBatchUnsubscribeCSVChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListBatchUnsubscribeCSVResultSet(response, path)

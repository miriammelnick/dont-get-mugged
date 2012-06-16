
###############################################################################
#
# ListBatchSubscribeCSV
# Adds or updates multiple subscribers in a given CSV file.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListBatchSubscribeCSV(Choreography):

    """
    Create a new instance of the ListBatchSubscribeCSV Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListBatchSubscribeCSV')


    def new_input_set(self):
        return ListBatchSubscribeCSVInputSet()

    def _make_result_set(self, result, path):
        return ListBatchSubscribeCSVResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListBatchSubscribeCSVChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListBatchSubscribeCSV
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListBatchSubscribeCSVInputSet(InputSet):
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
        Set the value of the DoubleOptIn input for this choreography. ((conditional, boolean) Flag to control whether a double opt-in confirmation message is sent. Specify '1' (true) or '0' (false). Defaults to 0.)
        """
        def set_DoubleOptIn(self, value):
            InputSet._set_input(self, 'DoubleOptIn', value)

        """
        Set the value of the EmailType input for this choreography. ((optional, string) Must be one of 'text', 'html', or 'mobile'. Defaults to html.)
        """
        def set_EmailType(self, value):
            InputSet._set_input(self, 'EmailType', value)

        """
        Set the value of the ListId input for this choreography. ((required, string) The id of the Mailchimp list associated with the email addresses to subscribe.)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the ReplaceInterests input for this choreography. ((optional, boolean) A flag to determine whether to replace the interest groups with the groups provided or add the provided groups to the member's interest groups. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        def set_ReplaceInterests(self, value):
            InputSet._set_input(self, 'ReplaceInterests', value)

        """
        Set the value of the SupressErrors input for this choreography. ((optional, boolean) Whether or not to suppress errors that arise from attempting to add/update a subscriber. Defaults to 0 (false). Set to 1 (true) to supress errors.)
        """
        def set_SupressErrors(self, value):
            InputSet._set_input(self, 'SupressErrors', value)

        """
        Set the value of the UpdateExisting input for this choreography. ((conditional, boolean) Indicates that if the email already exists, this request will perform an update instead of an insert. Specify '1' (true) or '0' (false). Defaults to 1.)
        """
        def set_UpdateExisting(self, value):
            InputSet._set_input(self, 'UpdateExisting', value)

        """
        Set the value of the VaultFile input for this choreography. (A path to a csv file in the vault containing the email addresses to unsubscribe. Can be used as an alternative to the CSVFile input.)
        """


"""
A ResultSet with methods tailored to the values returned by the ListBatchSubscribeCSV choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListBatchSubscribeCSVResultSet(ResultSet):
        """
        Retrieve the value for the "ErrorList" output from this choreography execution. ((multiline) A list of emails that were not successfully subscribed.)
        """
        def get_ErrorList(self):
            return self._output.get('ErrorList', None)
        """
        Retrieve the value for the "SuccessList" output from this choreography execution. ((multiline) A list of email successfully subscribed.)
        """
        def get_SuccessList(self):
            return self._output.get('SuccessList', None)

class ListBatchSubscribeCSVChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListBatchSubscribeCSVResultSet(response, path)

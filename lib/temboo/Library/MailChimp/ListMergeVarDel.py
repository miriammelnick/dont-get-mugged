
###############################################################################
#
# ListMergeVarDel
# Remove a field name from a MailChimp list.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListMergeVarDel(Choreography):

    """
    Create a new instance of the ListMergeVarDel Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/ListMergeVarDel')


    def new_input_set(self):
        return ListMergeVarDelInputSet()

    def _make_result_set(self, result, path):
        return ListMergeVarDelResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListMergeVarDelChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListMergeVarDel
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListMergeVarDelInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Mailchimp.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ListId input for this choreography. ((required, string) The id of the Mailchimp list associated with the merge var you want to delete.)
        """
        def set_ListId(self, value):
            InputSet._set_input(self, 'ListId', value)

        """
        Set the value of the Tag input for this choreography. ((required, string) Provide a valid merge var tag. A merge var tag can be retrieved by calling listMergeVars() or by logging in to your account.)
        """
        def set_Tag(self, value):
            InputSet._set_input(self, 'Tag', value)


"""
A ResultSet with methods tailored to the values returned by the ListMergeVarDel choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListMergeVarDelResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Mailchimp. Returns the string "true" for success and "false" for failures.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListMergeVarDelChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListMergeVarDelResultSet(response, path)

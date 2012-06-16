
###############################################################################
#
# Lists
# Get all lists from a MailChimp account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class Lists(Choreography):

    """
    Create a new instance of the Lists Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/MailChimp/Lists')


    def new_input_set(self):
        return ListsInputSet()

    def _make_result_set(self, result, path):
        return ListsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the Lists
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Mailchimp)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Indicates the desired format for the response. Accepted values are "json" or "xml" (the default).)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the Lists choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from Mailchimp. Corresponds to the format specified in the Output parameter. Defaults to "xml".)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListsResultSet(response, path)

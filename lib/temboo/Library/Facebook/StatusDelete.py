
###############################################################################
#
# StatusDelete
# Deletes a specified status message from the authenticated user's feed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class StatusDelete(Choreography):

    """
    Create a new instance of the StatusDelete Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Facebook/StatusDelete')


    def new_input_set(self):
        return StatusDeleteInputSet()

    def _make_result_set(self, result, path):
        return StatusDeleteResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return StatusDeleteChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the StatusDelete
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class StatusDeleteInputSet(InputSet):
        """
        Set the value of the AccessToken input for this choreography. ((required, string) The access token retrieved from the final step of the OAuth process.)
        """
        def set_AccessToken(self, value):
            InputSet._set_input(self, 'AccessToken', value)

        """
        Set the value of the StatusID input for this choreography. ((required, integer) The ID for the status message you want to delete.)
        """
        def set_StatusID(self, value):
            InputSet._set_input(self, 'StatusID', value)


"""
A ResultSet with methods tailored to the values returned by the StatusDelete choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class StatusDeleteResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((boolean) The response from Facebook. Returns "true" on success.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class StatusDeleteChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return StatusDeleteResultSet(response, path)

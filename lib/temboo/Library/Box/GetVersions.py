
###############################################################################
#
# GetVersions
# Retrieve the version history for a particular file stored in your Box.net account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class GetVersions(Choreography):

    """
    Create a new instance of the GetVersions Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/GetVersions')


    def new_input_set(self):
        return GetVersionsInputSet()

    def _make_result_set(self, result, path):
        return GetVersionsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetVersionsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the GetVersions
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class GetVersionsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Box.net.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AuthToken input for this choreography. ((required, string) Authorization Token retrieved by following the Oauth process described in Box.net API documentation.)
        """
        def set_AuthToken(self, value):
            InputSet._set_input(self, 'AuthToken', value)

        """
        Set the value of the TargetID input for this choreography. ((required, string) The ID of the file to retrieve version information for.)
        """
        def set_TargetID(self, value):
            InputSet._set_input(self, 'TargetID', value)


"""
A ResultSet with methods tailored to the values returned by the GetVersions choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class GetVersionsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class GetVersionsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return GetVersionsResultSet(response, path)

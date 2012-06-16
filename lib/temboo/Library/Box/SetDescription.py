
###############################################################################
#
# SetDescription
# Sets a description for a specified Box.net file or folder.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SetDescription(Choreography):

    """
    Create a new instance of the SetDescription Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Box/SetDescription')


    def new_input_set(self):
        return SetDescriptionInputSet()

    def _make_result_set(self, result, path):
        return SetDescriptionResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SetDescriptionChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SetDescription
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SetDescriptionInputSet(InputSet):
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
        Set the value of the Description input for this choreography. ((required, string) The description for Box.net file or folder.)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the TargetID input for this choreography. ((required, string) The Box.net ID of the file or folder you want to set a description for.)
        """
        def set_TargetID(self, value):
            InputSet._set_input(self, 'TargetID', value)

        """
        Set the value of the Target input for this choreography. ((required, string) They type of item to set a description for, either "file" (the default) or "folder".)
        """
        def set_Target(self, value):
            InputSet._set_input(self, 'Target', value)


"""
A ResultSet with methods tailored to the values returned by the SetDescription choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SetDescriptionResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Box.net.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SetDescriptionChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SetDescriptionResultSet(response, path)

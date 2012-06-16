
###############################################################################
#
# ListRealFolders
# Returns all existing RealFolders
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListRealFolders(Choreography):

    """
    Create a new instance of the ListRealFolders Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/ListRealFolders')


    def new_input_set(self):
        return ListRealFoldersInputSet()

    def _make_result_set(self, result, path):
        return ListRealFoldersResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListRealFoldersChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListRealFolders
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListRealFoldersInputSet(InputSet):
        """
        Set the value of the Login input for this choreography. ((string) Your RapidShare username)
        """
        def set_Login(self, value):
            InputSet._set_input(self, 'Login', value)

        """
        Set the value of the Password input for this choreography. ((string) Your RapidShare password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)


"""
A ResultSet with methods tailored to the values returned by the ListRealFolders choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListRealFoldersResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from RapidShare formatted in commas separated values.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListRealFoldersChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListRealFoldersResultSet(response, path)

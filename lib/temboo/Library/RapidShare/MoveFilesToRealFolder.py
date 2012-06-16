
###############################################################################
#
# MoveFilesToRealFolder
# Move an existing file to a new folder in RapidShare.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MoveFilesToRealFolder(Choreography):

    """
    Create a new instance of the MoveFilesToRealFolder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/MoveFilesToRealFolder')


    def new_input_set(self):
        return MoveFilesToRealFolderInputSet()

    def _make_result_set(self, result, path):
        return MoveFilesToRealFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MoveFilesToRealFolderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MoveFilesToRealFolder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MoveFilesToRealFolderInputSet(InputSet):
        """
        Set the value of the Files input for this choreography. ((integer) The id of the file to move. Can be a commas separated list of ids.)
        """
        def set_Files(self, value):
            InputSet._set_input(self, 'Files', value)

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
        Set the value of the RealFolder input for this choreography. ((optional, integer) The ID of the parent folder. Defaults to 0 for 'root'.)
        """
        def set_RealFolder(self, value):
            InputSet._set_input(self, 'RealFolder', value)


"""
A ResultSet with methods tailored to the values returned by the MoveFilesToRealFolder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MoveFilesToRealFolderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from RapidShare. The id of the newly created folder should be returned in the response upon a successful execution.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MoveFilesToRealFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MoveFilesToRealFolderResultSet(response, path)


###############################################################################
#
# MoveRealFolder
# Changes the parent ID of existing RealFolders, enabling the location of the folder to be moved within a RapidShare account file hierarchy.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class MoveRealFolder(Choreography):

    """
    Create a new instance of the MoveRealFolder Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/MoveRealFolder')


    def new_input_set(self):
        return MoveRealFolderInputSet()

    def _make_result_set(self, result, path):
        return MoveRealFolderResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return MoveRealFolderChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the MoveRealFolder
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class MoveRealFolderInputSet(InputSet):
        """
        Set the value of the FolderId input for this choreography. ((integer) The id of the folder(s) to be moved. Can be a commas separated list of ids.)
        """
        def set_FolderId(self, value):
            InputSet._set_input(self, 'FolderId', value)

        """
        Set the value of the Login input for this choreography. ((string) Your RapidShare username)
        """
        def set_Login(self, value):
            InputSet._set_input(self, 'Login', value)

        """
        Set the value of the NewParent input for this choreography. ((integer) Enter the ID of new parent folder)
        """
        def set_NewParent(self, value):
            InputSet._set_input(self, 'NewParent', value)

        """
        Set the value of the Password input for this choreography. ((string) Your RapidShare password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)


"""
A ResultSet with methods tailored to the values returned by the MoveRealFolder choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class MoveRealFolderResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from RapidShare. The id of the newly created folder should be returned in the response upon a successful execution.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class MoveRealFolderChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return MoveRealFolderResultSet(response, path)

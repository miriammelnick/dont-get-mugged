
###############################################################################
#
# RenameFile
# Renames a file to something else.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class RenameFile(Choreography):

    """
    Create a new instance of the RenameFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/RenameFile')


    def new_input_set(self):
        return RenameFileInputSet()

    def _make_result_set(self, result, path):
        return RenameFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return RenameFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the RenameFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class RenameFileInputSet(InputSet):
        """
        Set the value of the FileId input for this choreography. ((integer) The ID of the file to be renamed. Can be a commas separated list of ids.)
        """
        def set_FileId(self, value):
            InputSet._set_input(self, 'FileId', value)

        """
        Set the value of the Login input for this choreography. ((string) Your RapidShare username)
        """
        def set_Login(self, value):
            InputSet._set_input(self, 'Login', value)

        """
        Set the value of the NewFileName input for this choreography. ((string) The new file name.)
        """
        def set_NewFileName(self, value):
            InputSet._set_input(self, 'NewFileName', value)

        """
        Set the value of the Password input for this choreography. ((string) Your RapidShare password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)


"""
A ResultSet with methods tailored to the values returned by the RenameFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class RenameFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from RapidShare. The ID of the newly created folder should be returned in the response upon a successful execution.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class RenameFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return RenameFileResultSet(response, path)

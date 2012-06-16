
###############################################################################
#
# DeleteFiles
# Delete one or more files from RapidShare.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DeleteFiles(Choreography):

    """
    Create a new instance of the DeleteFiles Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/DeleteFiles')


    def new_input_set(self):
        return DeleteFilesInputSet()

    def _make_result_set(self, result, path):
        return DeleteFilesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DeleteFilesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DeleteFiles
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DeleteFilesInputSet(InputSet):
        """
        Set the value of the File input for this choreography. ((integer) The id of the file to delete. Can be a commas separated list of ids.)
        """
        def set_File(self, value):
            InputSet._set_input(self, 'File', value)

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
A ResultSet with methods tailored to the values returned by the DeleteFiles choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DeleteFilesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from RapidShare)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DeleteFilesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DeleteFilesResultSet(response, path)


###############################################################################
#
# ListFiles
# Lists the files in all folders (or in a specified folder) and allows you to control the database columns returned in the result.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListFiles(Choreography):

    """
    Create a new instance of the ListFiles Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/RapidShare/ListFiles')


    def new_input_set(self):
        return ListFilesInputSet()

    def _make_result_set(self, result, path):
        return ListFilesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListFilesChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListFiles
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListFilesInputSet(InputSet):
        """
        Set the value of the Fields input for this choreography. ((optional, string) The database columns to return separated by commas. (i.e. downloads,lastdownload,filename,size, etc))
        """
        def set_Fields(self, value):
            InputSet._set_input(self, 'Fields', value)

        """
        Set the value of the FileIDs input for this choreography. ((optional, integer) The id of the file to list. Multiple IDs can be entered separated by commas.)
        """
        def set_FileIDs(self, value):
            InputSet._set_input(self, 'FileIDs', value)

        """
        Set the value of the FileName input for this choreography. ((optional, string) The name of the file to list)
        """
        def set_FileName(self, value):
            InputSet._set_input(self, 'FileName', value)

        """
        Set the value of the FolderID input for this choreography. ((optional, integer) The id of the folder that contains the file you want to list. Defaults to 'all'.)
        """
        def set_FolderID(self, value):
            InputSet._set_input(self, 'FolderID', value)

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
A ResultSet with methods tailored to the values returned by the ListFiles choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListFilesResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((string) The response from RapidShare formatted in commas separated values.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListFilesChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListFilesResultSet(response, path)

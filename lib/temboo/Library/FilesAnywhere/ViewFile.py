
###############################################################################
#
# ViewFile
# Generate a URL from which a file can be viewed.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ViewFile(Choreography):

    """
    Create a new instance of the ViewFile Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/ViewFile')


    def new_input_set(self):
        return ViewFileInputSet()

    def _make_result_set(self, result, path):
        return ViewFileResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ViewFileChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ViewFile
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ViewFileInputSet(InputSet):
        """
        Set the value of the Path input for this choreography. ((required, string) Enter the path to the item being viewed in the following format: \USERNAME\file.txt)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)

        """
        Set the value of the Token input for this choreography. ((required, string) The token retrieved from authentication.  Can be passed from the AccountLogin Choreo.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the ViewFile choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ViewFileResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FilesAnywhere.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ViewFileChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ViewFileResultSet(response, path)

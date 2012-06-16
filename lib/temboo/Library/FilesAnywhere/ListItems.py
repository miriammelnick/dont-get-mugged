
###############################################################################
#
# ListItems
# Lists files within a specified directory in your FilesAnywhere account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class ListItems(Choreography):

    """
    Create a new instance of the ListItems Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/FilesAnywhere/ListItems')


    def new_input_set(self):
        return ListItemsInputSet()

    def _make_result_set(self, result, path):
        return ListItemsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListItemsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the ListItems
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class ListItemsInputSet(InputSet):
        """
        Set the value of the PageNum input for this choreography. ((optional, integer) The page number to return. Can be used to page through large result sets. Defaults to 1.)
        """
        def set_PageNum(self, value):
            InputSet._set_input(self, 'PageNum', value)

        """
        Set the value of the PageSize input for this choreography. ((optional, integer) The number of results to return per page. Defaults to 10.)
        """
        def set_PageSize(self, value):
            InputSet._set_input(self, 'PageSize', value)

        """
        Set the value of the Path input for this choreography. ((required, string) The path to the file you want to download (i.e. \JOHNSMITH\MyFolder\MyFile.txt).)
        """
        def set_Path(self, value):
            InputSet._set_input(self, 'Path', value)

        """
        Set the value of the Token input for this choreography. ((required, string) The token retrieved from authentication.  Can be passed from the AccountLogin Choreo.)
        """
        def set_Token(self, value):
            InputSet._set_input(self, 'Token', value)


"""
A ResultSet with methods tailored to the values returned by the ListItems choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class ListItemsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from FilesAnywhere.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class ListItemsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return ListItemsResultSet(response, path)

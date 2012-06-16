
###############################################################################
#
# SearchByCategory
# Retrieves a list of all resources in a category you specify.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchByCategory(Choreography):

    """
    Create a new instance of the SearchByCategory Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Google/Documents/SearchByCategory')


    def new_input_set(self):
        return SearchByCategoryInputSet()

    def _make_result_set(self, result, path):
        return SearchByCategoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchByCategoryChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchByCategory
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchByCategoryInputSet(InputSet):
        """
        Set the value of the Category input for this choreography. ((required, string) The category to list: "document", "spreadsheet", "presentation", "drawing", "folder", "starred", or "trashed". Combine multiple categories with "/".)
        """
        def set_Category(self, value):
            InputSet._set_input(self, 'Category', value)

        """
        Set the value of the MyDocs input for this choreography. ((optional, boolean) Enter "true" to return resources for the requesting user only. The default is "false" (returns all account resources).)
        """
        def set_MyDocs(self, value):
            InputSet._set_input(self, 'MyDocs', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Google account password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your Google account username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)

        """
        Set the value of the Viewed input for this choreography. ((optional, boolean) Enter "true" to return only viewed resources for the specified category. The default is "false" (viewed and unviewed category resources).)
        """
        def set_Viewed(self, value):
            InputSet._set_input(self, 'Viewed', value)


"""
A ResultSet with methods tailored to the values returned by the SearchByCategory choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchByCategoryResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from the Google Documents API.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchByCategoryChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchByCategoryResultSet(response, path)


###############################################################################
#
# DocumentsListAndSearch
# Search and return a list of documents from OfficeDrop
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class DocumentsListAndSearch(Choreography):

    """
    Create a new instance of the DocumentsListAndSearch Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/OfficeDrop/DocumentsListAndSearch')


    def new_input_set(self):
        return DocumentsListAndSearchInputSet()

    def _make_result_set(self, result, path):
        return DocumentsListAndSearchResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DocumentsListAndSearchChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the DocumentsListAndSearch
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class DocumentsListAndSearchInputSet(InputSet):
        """
        Set the value of the Favorites input for this choreography. ((optional, boolean) Will return documents that have been marked as favorites. Specify a 1 for true. Defaults to 0.)
        """
        def set_Favorites(self, value):
            InputSet._set_input(self, 'Favorites', value)

        """
        Set the value of the FolderId input for this choreography. ((optional, integer) The ID of the folder to filter by.)
        """
        def set_FolderId(self, value):
            InputSet._set_input(self, 'FolderId', value)

        """
        Set the value of the LabelIds input for this choreography. ((optional, integer) A comma separated list of label IDs to filter the result by.)
        """
        def set_LabelIds(self, value):
            InputSet._set_input(self, 'LabelIds', value)

        """
        Set the value of the Page input for this choreography. ((optional, integer) The page of the documents listing you want to return. Defaults to 1.)
        """
        def set_Page(self, value):
            InputSet._set_input(self, 'Page', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your OfficeDrop password.)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the PerPage input for this choreography. ((optional, integer) The number of documents you want to return in each request. Defaults to 15.)
        """
        def set_PerPage(self, value):
            InputSet._set_input(self, 'PerPage', value)

        """
        Set the value of the Query input for this choreography. ((optional, string) The text keywords to search by.)
        """
        def set_Query(self, value):
            InputSet._set_input(self, 'Query', value)

        """
        Set the value of the Sort input for this choreography. ((optional, string) The method you want to sort the results by: newest, oldest, most_viewed, name, name_reverse, recently_viewed, most_viewed, or relevance.)
        """
        def set_Sort(self, value):
            InputSet._set_input(self, 'Sort', value)

        """
        Set the value of the Username input for this choreography. ((required, string) Your OfficeDrop username.)
        """
        def set_Username(self, value):
            InputSet._set_input(self, 'Username', value)


"""
A ResultSet with methods tailored to the values returned by the DocumentsListAndSearch choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class DocumentsListAndSearchResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from OfficeDrop.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class DocumentsListAndSearchChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return DocumentsListAndSearchResultSet(response, path)

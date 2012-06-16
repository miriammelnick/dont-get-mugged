
###############################################################################
#
# LiteracyAndLanguage
# Returns results for projects within the Literacy and Language category.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LiteracyAndLanguage(Choreography):

    """
    Create a new instance of the LiteracyAndLanguage Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DonorsChoose/LiteracyAndLanguage')


    def new_input_set(self):
        return LiteracyAndLanguageInputSet()

    def _make_result_set(self, result, path):
        return LiteracyAndLanguageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LiteracyAndLanguageChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LiteracyAndLanguage
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LiteracyAndLanguageInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((optional, string) The APIKey provided by Donor's Choose. Defaults to the test  APIKey 'DONORSCHOOSE'.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Index input for this choreography. ((optional, integer) The number of the first row to return in the result. For example, if index=10, the results could show rows 10-59.)
        """
        def set_Index(self, value):
            InputSet._set_input(self, 'Index', value)

        """
        Set the value of the Max input for this choreography. ((optional, integer) The max number of projects to return. Can return up to 50 rows at a time. Defaults to 10 when left empty.)
        """
        def set_Max(self, value):
            InputSet._set_input(self, 'Max', value)

        """
        Set the value of the ShowCounts input for this choreography. ((optional, boolean) Set to 1 to return facet counts in the response)
        """
        def set_ShowCounts(self, value):
            InputSet._set_input(self, 'ShowCounts', value)

        """
        Set the value of the ShowSynopsis input for this choreography. ((optional, boolean) Set to 1 to show the synopsis for each project listing)
        """
        def set_ShowSynopsis(self, value):
            InputSet._set_input(self, 'ShowSynopsis', value)

        """
        Set the value of the Subject input for this choreography. ((optional, string) Enter a sub-category of Literacy & Language. When left empty, all Literacy & Language projects are returned.)
        """
        def set_Subject(self, value):
            InputSet._set_input(self, 'Subject', value)


"""
A ResultSet with methods tailored to the values returned by the LiteracyAndLanguage choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LiteracyAndLanguageResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Donor's Choose)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LiteracyAndLanguageChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LiteracyAndLanguageResultSet(response, path)

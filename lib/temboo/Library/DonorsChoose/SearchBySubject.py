
###############################################################################
#
# SearchBySubject
# Sub-Choreo used for all other thin wrapper Choreos for Donor's Choose API.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class SearchBySubject(Choreography):

    """
    Create a new instance of the SearchBySubject Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/DonorsChoose/SearchBySubject')


    def new_input_set(self):
        return SearchBySubjectInputSet()

    def _make_result_set(self, result, path):
        return SearchBySubjectResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SearchBySubjectChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the SearchBySubject
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class SearchBySubjectInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ()
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the Index input for this choreography. ()
        """
        def set_Index(self, value):
            InputSet._set_input(self, 'Index', value)

        """
        Set the value of the Keywords input for this choreography. ()
        """
        def set_Keywords(self, value):
            InputSet._set_input(self, 'Keywords', value)

        """
        Set the value of the Max input for this choreography. ()
        """
        def set_Max(self, value):
            InputSet._set_input(self, 'Max', value)

        """
        Set the value of the ShowCounts input for this choreography. ()
        """
        def set_ShowCounts(self, value):
            InputSet._set_input(self, 'ShowCounts', value)

        """
        Set the value of the ShowSynopsis input for this choreography. ()
        """
        def set_ShowSynopsis(self, value):
            InputSet._set_input(self, 'ShowSynopsis', value)

        """
        Set the value of the SubjectCategory input for this choreography. ()
        """
        def set_SubjectCategory(self, value):
            InputSet._set_input(self, 'SubjectCategory', value)

        """
        Set the value of the Subject input for this choreography. ()
        """
        def set_Subject(self, value):
            InputSet._set_input(self, 'Subject', value)


"""
A ResultSet with methods tailored to the values returned by the SearchBySubject choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class SearchBySubjectResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ()
        """
        def get_Response(self):
            return self._output.get('Response', None)

class SearchBySubjectChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return SearchBySubjectResultSet(response, path)

header_dir = $(COMMON_HEAD_DIR)
lib_dir = $(COMMON_LIB_DIR)
LIBS = $(COMMON_LIBS)

LIBSEAL= ../base/libseal.a

CXXFLAGS = $(SEAL_COMPILE_OPT)  -D_GNU_SOURCE -D_REENTRANT $(header_dir)
CXXLFLAGS = $(SEAL_COMPILE_OPT) -Wall $(lib_dir) $(LIBS)

objects = Main.o SuperServer.o ServerTask.o

SRCS = $(objects:%.o=%.cpp)
DEPS = $(objects:%.o=.%.d)

ALL_TARGETS = SuperServer

all: $(ALL_TARGETS)

include $(DEPS)
$(DEPS): .%.d: %.cpp
	@$(CXX) -M $(CXXFLAGS) $< > $@.$$$$; sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; rm -f $@.$$$$

$(objects): %.o: %.cpp
	$(CXX) -c $(CXXFLAGS) $< -o $@

$(ALL_TARGETS): $(objects) $(LIBSEAL)
	$(CXX) $(objects) -o $@ $(CXXLFLAGS)

clean:
	@rm -rf *.o .*.d* $(ALL_TARGETS) core *~
